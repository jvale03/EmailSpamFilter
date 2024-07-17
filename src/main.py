from DataPreprocessing import preprocess_dataset, preprocess_file
import NaiveBayesAlgorithm as NBA

def main():
    choice = 0
    while True:
        print("---------------")
        choice = input("1: Preprocess data\n2: Train & test data\n3: Get model report\n4: Test input with saved model\n5: Exit\nSelect option: ")
        if choice.isdigit():
            choice = int(choice)
            if choice > 5 or choice < 1:
                print("\033[31mInvalid!\033[m")
            else:
                print("---------------")
                if choice == 1:
                    preprocess_dataset()

                elif choice == 2:
                    print("\033[32mTesting model...\033[m")
                    model = NBA.naive_bayes()
                    print("Report:")
                    print(model[3])
                    true_false = input(f"Save model? y/n: ")

                    if true_false == "y" or true_false == "":
                        NBA.save_model(model)

                elif choice == 3:
                    NBA.get_report()
                
                elif choice == 5:
                    break
        else:
            print("\033[31mInvalid!\033[m")

main()