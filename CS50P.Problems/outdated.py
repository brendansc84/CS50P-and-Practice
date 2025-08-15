def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    
    
    while True:
        try:
            date = input("Date: ").strip()
            
            if "," in date:
                date = date.replace(",", "")
                month_name, day, year = date.split()
                month = months[month_name.title()]
            else:
                parts = [p.strip() for p in date.split("/")]
                if len(parts) != 3:
                    raise ValueError
                month, day, year = parts
                
            month = int(month)
            day = int(day)
            year = int(year)

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError
            else:
                print(f"{year}-{month:02}-{day:02}")
            break
        except (ValueError, KeyError):
            continue

if __name__ == "__main__":
    main()