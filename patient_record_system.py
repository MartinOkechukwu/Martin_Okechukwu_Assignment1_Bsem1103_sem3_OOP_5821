
"""
Patient Record Management System
PROG211 - Object-Oriented Programming 1

"""


class Patient:
    """Represents one patient."""

    def __init__(self, patient_id, name, age, reason):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.reason = reason

    # Instance method
    def update_record(self, name=None, age=None, reason=None):
        if name is not None and name.strip():
            self.name = name.strip()

        if age is not None:
            if not Patient.is_valid_age(age):
                return False
            self.age = age

        if reason is not None and reason.strip():
            self.reason = reason.strip()

        return True

    # Instance method
    def display_info(self):
        print("-" * 40)
        print(f"Patient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Visit Reason: {self.reason}")
        print("-" * 40)

    # Static method
    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 <= age <= 120


class PatientRecordSystem:
    """Manages multiple patient objects."""

    total_registered = 0

    def __init__(self):
        # Python list stores Patient objects.
        self.patients = []

    # Class method
    @classmethod
    def get_total_registered(cls):
        return cls.total_registered

    # Instance method
    def add_patient(self, patient):
        if self.find_patient(patient.patient_id) is not None:
            print("Error: This patient ID already exists.")
            return False

        self.patients.append(patient)
        PatientRecordSystem.total_registered += 1
        print("Patient registered successfully.")
        return True

    # Instance method
    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id.lower() == patient_id.lower():
                return patient
        return None

    # Instance method
    def display_all_patients(self):
        if not self.patients:
            print("No patient records found.")
            return

        print("\nALL PATIENT RECORDS")
        for patient in self.patients:
            patient.display_info()

    # Instance method
    def search_patient(self, patient_id):
        patient = self.find_patient(patient_id)

        if patient is None:
            print("Patient not found.")
        else:
            print("\nPATIENT FOUND")
            patient.display_info()

    # Instance method
    def update_patient(self, patient_id):
        patient = self.find_patient(patient_id)

        if patient is None:
            print("Patient not found.")
            return

        print("Leave a field empty to keep its current value.")

        name = input(f"New name [{patient.name}]: ").strip()
        age_text = input(f"New age [{patient.age}]: ").strip()
        reason = input(
            f"New visit reason [{patient.reason}]: "
        ).strip()

        new_age = None

        if age_text:
            try:
                new_age = int(age_text)
            except ValueError:
                print("Age must be a whole number.")
                return

        if patient.update_record(
            name=name or None,
            age=new_age,
            reason=reason or None
        ):
            print("Patient record updated successfully.")
        else:
            print("Invalid age. Record was not updated.")


def main():
    system = PatientRecordSystem()

    # Fictional sample records for demonstration.
    system.add_patient(
        Patient("P001", "John Kamara", 25, "General check-up")
    )
    system.add_patient(
        Patient("P002", "Mary Conteh", 32, "Headache")
    )

    while True:
        print("\n================================")
        print(" PATIENT RECORD MANAGEMENT SYSTEM")
        print("================================")
        print("1. Register a patient")
        print("2. Display all patients")
        print("3. Search for a patient")
        print("4. Update a patient record")
        print("5. Count registered patients")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            patient_id = input("Enter patient ID: ").strip()
            name = input("Enter patient name: ").strip()
            age_text = input("Enter patient age: ").strip()
            reason = input("Enter visit reason: ").strip()

            if not all([patient_id, name, age_text, reason]):
                print("All fields are required.")
                continue

            try:
                age = int(age_text)
            except ValueError:
                print("Age must be a whole number.")
                continue

            if not Patient.is_valid_age(age):
                print("Enter a valid age between 0 and 120.")
                continue

            patient = Patient(patient_id, name, age, reason)
            system.add_patient(patient)

        elif choice == "2":
            system.display_all_patients()

        elif choice == "3":
            patient_id = input("Enter patient ID to search: ").strip()
            system.search_patient(patient_id)

        elif choice == "4":
            patient_id = input("Enter patient ID to update: ").strip()
            system.update_patient(patient_id)

        elif choice == "5":
            print(
                "Registered patients:",
                system.get_total_registered()
            )

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option. Please choose from 1 to 6.")


if __name__ == "__main__":
    main()
