from data_loader import load_data
from preprocessing import preprocess

def main():
    data = load_data()
    X, y, scaler = preprocess(data)
    print("Data ready for training:", X.shape)

if __name__ == "__main__":
    main()
