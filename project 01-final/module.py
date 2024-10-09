import struct,os,collections
"""
[Id,Name,year,type,price]
"""
# ANSI color
Red = '\033[31m'
Green = '\033[32m'
Blue = '\033[34m'
Yellow = '\033[33m'
Reset = '\033[0m'

# Done!!
def save_records(filePath):

    with open(filePath,"wb") as file:
        r_count = 0
        try:
            count = int(input("How many record you want to create?: "))
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        else:
            for i in range(count):
                try:
                    print(f"Recod Number #{r_count +1}")
                    id = int(input("ID: "))
                    name = input("Name: ")
                    year = int(input("Year: "))
                    cdType = input("Type: ")
                    price = float(input("Price: "))
                
                except ValueError as e:
                    print(f"Error: {e}")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    break
                
                else:
                    data = struct.pack("i20si20sf",id,name.encode(),year,cdType.encode(),price)
                    file.write(data)
                    r_count += 1
                    print()
                
            print(Green + f"Done!! {r_count} record has been created" + Reset)

# Done!!
def add_records(filePath):
    check = os.path.exists(filePath)
    if check != True:
        print("Error: File Not Found!!")
    
    else:
        with open(filePath,"ab") as file:
            r_count = 0
            try:
                count = int(input("How many record you want to create?: "))
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
            else:
                for i in range(count):
                    try:
                        print(f"Record Number #{r_count+1}")
                        id = int(input("ID: "))
                        name = input("Name: ")
                        year = int(input("Year: "))
                        cdType = input("Type: ")
                        price = float(input("Price: "))
                    
                    except ValueError as e:
                        print(f"Error: {e}")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                        break
                    
                    else:
                        data = struct.pack("i20si20sf",id,name.encode(),year,cdType.encode(),price)
                        file.write(data)
                        r_count += 1
                        print()
                    
                print(Green + f"Done!! {r_count} record has been created" + Reset)

# Done!!
def read_records(filePath: str) -> None:
    if not os.path.exists(filePath):
        print("Error: File Not Found!!")
        return

    with open(filePath, "rb") as file:
        print(Green + "Result:" + Reset)
        print("______________________________________________________________________")
        
        while True:
            record = file.read(struct.calcsize("i20si20sf"))
            if not record:
                break
            
            record = struct.unpack("i20si20sf", record)
            record = (
                record[0],                      # ID (int)
                record[1].decode().strip(),     # Name (str)
                record[2],                      # Year (int)
                record[3].decode().strip(),     # Type (str)
                record[4]                       # Price (float)
            )

            print(f"[ID: {record[0]}, Name: {record[1]}, Year: {record[2]}, Type: {record[3]}, Price: {record[4]:.2f}$]")

        print("______________________________________________________________________")
        print()

# Done!!
def find_records(filePath) ->str:
    check = os.path.exists(filePath)
    if check != True:
        print("Error: File Not Found!!")
    
    else:
        find = input('Which record are you looking for? (id,name,year,type,price): ')
        print(Green + "Result:" + Reset)
        print("______________________________________________________________________")
        n_record = {}
        count = 1
        oo = 0
        with open(filePath,"rb") as file:
            while True:
                record = file.read(struct.calcsize("i20si20sf"))
                if not record:
                    break
                else:
                    record = struct.unpack("i20si20sf",record)
                    record = record[0],record[1].decode(),record[2],record[3].decode(),record[4]
                    n_record[count] = (f"[ID:{record[0]}, Name:{record[1]}, Year:{record[2]}, Type:{record[3]}, Price:{record[4]:.2f}$]")
                    count += 1
        
        for key,value in n_record.items():
            if find in value:
               print(value)
               oo += 1
            else:
               continue
        if oo == 0:
            print(Red + f"Not found [{find}] in any records" + Reset)
        print("______________________________________________________________________")
        print()
 
# Done!!
def del_file_record(filePath):
    check = os.path.exists(filePath)
    if check != True:
        print("Error: File Not Found!!")
    else:
        q = input("Confirm type (Yes,No): ")
        if q.lower() == "yes":
            os.remove(filePath)
            print(Green + f"{filePath} Removed!!" + Reset)
        else:
            print(Red + "Removing has been Stoped!!" + Reset)
    print()

# Done!!
def edit_record(file):
    if not os.path.exists(file):
        print("Error: File Not Found!")
        return

    records = []
    record_size = struct.calcsize("i20si20sf")

    with open(file, "rb") as file_obj:
        while True:
            record = file_obj.read(record_size)
            if not record:
                break
            records.append(struct.unpack("i20si20sf", record))

    print(Green + "Current Records:" + Reset)
    print("______________________________________________________________________")
    for idx, record in enumerate(records):
        name = record[1].decode().strip()
        id = record[0]
        year = record[2]
        _type = record[3].decode().strip()
        price = record[4]
        print(f"{idx + 1}: [Id: {id}, Name: {name}, Year: {year}, Type: {_type}, Price: {price:.2f}$]")
    print("______________________________________________________________________")
    try:
        index = int(input("Enter the record number you want to edit: ")) - 1
        if index < 0 or index >= len(records):
            print("Error: Invalid record number.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return

    record_to_edit = records[index]
    id = record_to_edit[0]
    name = record_to_edit[1].decode().strip()
    year = record_to_edit[2]
    _type = record_to_edit[3].decode().strip()
    price = record_to_edit[4]

    print(f"\nEditing record {index + 1}: [Id: {id}, Name: {name}, Year: {year}, Type: {_type}, Price: {price:.2f}$]")

    new_id = input(f"New ID (leave blank to not change): ")
    new_name = input(f"New Name (leave blank to not change): ")
    new_year = input(f"New Year (leave blank to not change): ")
    new_type = input(f"New Type (leave blank to not change): ")
    new_price = input(f"New Price (leave blank to not change): ")

    new_id = int(new_id) if new_id else id
    new_name = new_name.encode() if new_name.strip() else record_to_edit[1]
    new_year = int(new_year) if new_year else year
    new_type = new_type.encode() if new_type.strip() else record_to_edit[3]
    new_price = float(new_price) if new_price else price


    records[index] = (new_id, new_name, new_year, new_type, new_price)

    with open(file, "wb") as file_obj:
        for record in records:
            file_obj.write(struct.pack("i20si20sf", *record))

    print(Green + "Record updated successfully!" + Reset)
    print()

# Done!!
def remove_records(file):
    if not os.path.exists(file):
        print("Error: File Not Found!")
        return

    records = []
    record_size = struct.calcsize("i20si20sf")

    with open(file, "rb") as file_obj:
        while True:
            record = file_obj.read(record_size)
            if not record:
                break
            records.append(struct.unpack("i20si20sf", record))

    print(Green + "Current Records:" + Reset)
    print("______________________________________________________________________")
    for idx, record in enumerate(records):
        name = record[1].decode().strip()
        id = record[0]
        year = record[2]
        _type = record[3].decode().strip()
        price = record[4]
        print(f"{idx + 1}: [Id: {id}, Name: {name}, Year: {year}, Type: {_type}, Price: {price:.2f}$]")
    print("______________________________________________________________________")

    try:
        index = int(input("Enter the record number you want to remove: ")) - 1
        if index < 0 or index >= len(records):
            print("Error: Invalid record number.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return
    
    confirm = input(f"Are you sure you want to remove the record? (yes/no): ").strip().lower()

    if confirm == 'yes':
        del records[index]
        with open(file, "wb") as file_obj:
            for record in records:
                file_obj.write(struct.pack("i20si20sf", *record))
            print(Green + "Record removed successfully!" + Reset)
            print()
    
    elif confirm == 'no':
        print(Red + "Record removal canceled." + Reset)
        print()
    else:
        print("Invalid input. Please respond with 'yes' or 'no'.")
        print()
    
# Done!!
def find_max_min(n_list,choice):
        y = 0
        n = ""
        for i in range(len(n_list["Year"])): 
            s_year = n_list["Year"][i] 
            s_name = n_list["Name"][i] 
            match choice:
                case "max":
                    if s_year > y: 
                        y = s_year  
                        n = s_name
                
                case "min":
                    if y == 0: 
                        y = s_year  
                        n = s_name
                    elif s_year < y:
                        y = s_year  
                        n = s_name
        return y,n
def find_expensive(n_list):
    p = 0
    n = ""
    for i in range(len(n_list["Price"])): 
        s_price = n_list["Price"][i] 
        s_name = n_list["Name"][i] 
        
        if s_price > p: 
            p = s_price  
            n = s_name

    return n,p
# Done!!
def summary_Report(filePath):
    report = {}
    numR = 0
    
    check = os.path.exists(filePath)
    if check != True:
        print("Error: File Not Found!!")
    
    else:
        with open(filePath,"rb") as file:
            while True:
                record = file.read(struct.calcsize("i20si20sf"))
                if not record:
                    break
                else:
                    record = struct.unpack("i20si20sf",record)
                    record = record[0],record[1].decode(),record[2],record[3].decode(),record[4]
                    
                    if "Id" not in report:
                        report["Id"] = [(record[0])]
                        report["Name"] = [(record[1])]
                        report["Year"] = [(record[2])]
                        report["Type"] = [(record[3])]
                        report["Price"] = [(record[4])]
                        numR += 1

                    else:
                        report["Id"].append(record[0])
                        report["Name"].append(record[1])
                        report["Year"].append(record[2])
                        report["Type"].append(record[3])
                        report["Price"].append(record[4])
                        numR += 1
                        
    report['Name'] = [name.replace('\x00', '') for name in report["Name"]]
    report['Type'] = [t.replace('\x00', '') for t in report['Type']]

    allP = sum([p for p in report["Price"]])
    allT = dict(collections.Counter([t for t in report["Type"]]))
    newM = find_max_min(report,"max")
    oldM = find_max_min(report,"min")
    expenM = find_expensive(report)
        
    print(f"""
:{Green + "Report Summary" + Reset}:
______________________________________________________________________
[Number of Records stroed: {numR}]
[Total value : {allP:.2f}$]
[The most enpensive product : {expenM[0]}, {expenM[1]:.2f}$]
[Total Product Type : {allT}]
[Newest Movie : {newM[1]}, {newM[0]}]
[Oldest Movie : {oldM[1]}, {oldM[0]}]
______________________________________________________________________
""")