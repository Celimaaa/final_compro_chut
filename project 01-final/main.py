import module as md

# ANSI color
Red = '\033[31m'
Green = '\033[32m'
Blue = '\033[34m'
Yellow = '\033[33m'
Reset = '\033[0m'

def Run():
    runing = True

    print("____Welcome!!!____\nMovie Store Record")
    #filePath = input("File Path: ")
    filePath = "cd_record.bin"
    print("──────────────────")
    print("1.Create new File record\n2.Add new records\n3.Show records\n4.Edit record\n5.Find records\n6.Summary Report\n7.Remove record\n8.Delete file record\n9.Quit")
    print("──────────────────")
    while runing:
        choice = input("Type your action (1 - 9) (0 for action list): ")
        while True:     
            if choice not in ["0","1","2","3","4","5","6","7","8","9"]:
                print(Red + "Error: ValueError { Please Enter 1 to 9 }!!" + Reset)
                break
            else:
                match choice:
                    case "0":
                        print("──────────────────")
                        print("1.Create new File record\n2.Add new records\n3.Show records\n4.Edit record\n5.Find records\n6.Summary Report\n7.Remove record\n8.Delete file record\n9.Quit")
                        print("──────────────────")
                        print()
                        break
                    case "1":
                        md.save_records(filePath)
                        break
                    case "2":
                        md.add_records(filePath)
                        break
                    case "3":
                        md.read_records(filePath)
                        break
                    case "4":
                        md.edit_record(filePath)
                        break
                    case"5":
                        md.find_records(filePath)
                        break
                    case "6":
                        md.summary_Report(filePath)
                        break
                    case "7":
                        md.remove_records(filePath)
                        break
                    case "8":
                        md.del_file_record(filePath)
                        break
                    case "9":
                        runing = False
                        print(Green + "Quit successfully!!!" + Reset)
                        break

if __name__ == "__main__":
    Run()