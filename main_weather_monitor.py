import model
from test_weather import run_all_tests

def main() -> None:
    run_all_tests()
    while True:
        the_city=input("Enter the city you want to know information about (or type 'exit' to quit):\n")
        if the_city.lower() == 'exit':
            print("Goodbye.")
            break
        model.get_weather(f"{the_city}")

if __name__ == "__main__":
    main()