from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')   # Fix for graph display
import matplotlib.pyplot as plt


class Patient:
    def __init__(self, pid, name, age, gender):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.ward = None

    def display(self):
        print(f"{self.pid} | {self.name} | {self.age} | {self.gender} | {self.ward}")


class Ward:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def assign(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.ward = self.name
            print("Assigned to", self.name)
        else:
            print("Ward Full!")
 class Admission:
    def __init__(self, patient):
        self.patient = patient
        self.admit_date = datetime.now()
        self.discharge_date = None
    def discharge(self):
        self.discharge_date = datetime.now()
    def stay_days(self):
        if self.discharge_date:
            return max(1, (self.discharge_date - self.admit_date).days)
        return 0
 class Billing:
    def __init__(self, patient, days):
        self.patient = patient
        self.days = days
        self.rate = 1000
        self.total = self.days * self.rate
    def display(self):
        print(f"Bill for {self.patient.name}: ₹{self.total}")
 patients = {}
 unique_ids = set()
 admissions = []

 general = Ward("General", 3)
 icu = Ward("ICU", 2)
 def add_patient():
    pid = input("ID: ")
    if pid in unique_ids:
        print("ID exists!")
        return
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    p = Patient(pid, name, age, gender)
    patients[pid] = p
    unique_ids.add(pid)
    ward = input("Ward (1-General, 2-ICU): ")
    if ward == "1":
        general.assign(p)
    elif ward == "2":
        icu.assign(p)
 def admit_patient():
     pid = input("Enter Patient ID: ")
     if pid in patients:
        a = Admission(patients[pid])
        admissions.append(a)
        print("Admitted")
    else:
        print("Not found")
 def discharge_patient():
    pid = input("Enter Patient ID: ")
    for a in admissions:
        if a.patient.pid == pid and a.discharge_date is None:
            a.discharge()
            days = a.stay_days()
            print("Discharged. Stay:", days, "days")
            bill = Billing(a.patient, days)
            bill.display()
            return
    print("No active admission")
 def display_patients():
    for p in patients.values():
        p.display()
 def analytics():
     stays = [a.stay_days() for a in admissions if a.discharge_date]
    if len(stays) == 0:
        print("No data")
        return
    avg = sum(stays) / len(stays)
    print("Average Stay:", avg)
    print("Plotting graphs...")
    plt.figure()
    plt.bar(range(len(stays)), stays)
    plt.title("Bar Chart - Patient Stay")
    plt.xlabel("Patients")
    plt.ylabel("Days")
    plt.show(block=True)
    plt.figure()
    plt.plot(stays, marker='o')
    plt.title("Line Graph - Stay Trend")
    plt.xlabel("Patients")
    plt.ylabel("Days")
    plt.show(block=True)
    plt.figure()
    plt.pie(stays, labels=[f"P{i+1}" for i in range(len(stays))], autopct='%1.1f%%')
    plt.title("Pie Chart - Stay Distribution")
    plt.show(block=True)
    # SCATTER
    plt.subplot(2, 2, 4)
    plt.scatter(range(len(stays)), stays)
    plt.title("Scatter Plot - Stay Pattern")
    plt.xlabel("Patients")
    plt.ylabel("Days")
    plt.tight_layout()
    plt.show()
while True:
    print("\n1.Add Patient")
    print("2.Display Patients")
    print("3.Admit Patient")
    print("4.Discharge Patient")
    print("5.Analytics")
    print("6.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_patient()
    elif ch == "2":
        display_patients()
    elif ch == "3":
        admit_patient()
    elif ch == "4":
        discharge_patient()
    elif ch == "5":
        analytics()
    elif ch == "6":
        break
    else:
        print("Invalid")
