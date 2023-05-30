import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer= csv.writer(csv_file)
        if csv_file.tell() == 0
        writer.writerow(["Name","Age","Contact number","E-mail ID"])
        writer.writerow(info_list)
if __name__ == '__main__':
 conditon = True
 student_num_=1
 while(conditon):
     student_info= input("Enter student information int he following format (Name Age Contact_number E-mai_ID): ")
     print("Entered Information: " + student_info)
     student_info_list= student_info.split(' ')
     print("\nEntered information is: \n Name: {}\n Age: {} \n Contact_Number: {}\n E-mail_ID: {}" .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
     
     choice_check= input("Is the entered information correct? (yes/no): ")
     if choice_check == "yes":
         write_into_csv(student_info_list)

         conditon_check= input("Enter yes/no if you want to input information for another student: ")

         if conditon_check == "yes":
              conditon=True

         elif conditon_check == "no":
              conditon=False

     elif choice_check == "no":
         print("\nPlease re-enter the values!")

