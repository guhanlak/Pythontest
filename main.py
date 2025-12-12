import datetime

def main():
    now = datetime.datetime.utcnow()
    print("🚀 Script is running on Railway!")
    print("UTC Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
