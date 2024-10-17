from ecosystem import Ecosystem

def main():
    ecosystem = Ecosystem(15)
    ecosystem.populate(5, 4)
    ecosystem.display_river()
    ecosystem.run_simulation(10)

if __name__ == "__main__":
    main()