from S1E9 import Character, Stark


def test():
    """other test"""
    hodor = Character("hodor")
    print(hodor.__dict__)
    print(hodor.is_alive)
    hodor.die()
    print(hodor.is_alive)
    print(hodor.__doc__)
    print(hodor.__init__.__doc__)
    print(hodor.die.__doc__)
    print("---")


def main():
    """subject test"""
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)

        test()
    except Exception as e:
        print("Exception Error:", e)


if __name__ == "__main__":
    main()
