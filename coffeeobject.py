"""
Example OOP program for something
"""
class CoffeeBagIGuess:
    """
    Represents coffee, I guess
    """
    def __init__(self, growing_location: str, name: str, weight_grams: int) -> None:
        """
        Initialize the supplied coffee
        bag instance
        """
        self.growing_location: str = growing_location
        self.name: str = name
        self.weight_grams: int = weight_grams
        print("New coffee")

    def __str__(self) -> str:
        """
        Provides easily understandable info abt the coffee
        """
        return f"{self.weight_grams}g of {self.name}, from {self.growing_location}"
     
    def brew(self, grams_used: int)-> None:
        """
        Brews ts coffee
        """
        if grams_used>self.weight_grams:
            print("Haha stupid kys")
        else:
            self.weight_grams-=grams_used
            print(f"{grams_used}g of {self.name} used.")



def main() -> None:
    """
    Number 1 app of all time
    """
    current_bag: CoffeeBagIGuess = CoffeeBagIGuess("Ethiopia", "Ethiopian Coffee", 1000)
    favorite_bag: CoffeeBagIGuess = CoffeeBagIGuess("Chud Island", "Chud Coffee", 670)

    favorite_bag.brew(100)

    print(f"Current bag: {current_bag}.")
    print(f"Favorite bag: {favorite_bag}.")

if __name__ == "__main__":
    main()
