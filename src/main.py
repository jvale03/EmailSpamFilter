from DataPreprocessing import preprocess_dataset, preprocess_file, clean_text
import NaiveBayesAlgorithm as NBA

def main():
    choice = 0
    while True:
        print("---------------")
        choice = input("1: Preprocess data\n2: Train & test data\n3: Get model report\n4: Test input with saved model\nSelect option: ")
        if choice.isdigit():
            choice = int(choice)
            if choice > 5 or choice < 1:
                print("\033[31mInvalid!\033[m")
            else:
                    break
        else:
            print("\033[31mInvalid!\033[m")
        
    print("---------------")
    if choice == 1:
        preprocess_dataset()

    elif choice == 2:
        print("\033[32mTesting model...\033[m")
        model = NBA.naive_bayes()
        if model!=None:
            print("Report:")
            print(model[3])
            true_false = input(f"Save model? y/n: ")

            if true_false == "y" or true_false == "":
                NBA.save_model(model)

    elif choice == 3:
        NBA.get_report()
    
    elif choice == 4:
        # test
        with open("input.txt","r") as file:
            content = file.read()
            content = clean_text(content)
        
        result = NBA.test_input([content])

        if result != None and result == 0:
            print("\033[32mThis email is not spam!\033[m")
        elif result != None and result == 1:
            print("\033[31mThis email is spam!\033[m")

main()