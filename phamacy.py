class Pharmacy:
    pharmacy_name = "City Pharmacy"  # Static attribute
    available_medicines = []         # قائمة الأدوية المتاحة
    sold_medicines = []              # قائمة الأدوية المباعة
    needed_medicines = []            # قائمة الأدوية المطلوبة

    def __init__(self, name, quantity, price, expiration_date):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.expiration_date = expiration_date

    @staticmethod
    def get_pharmacy_info():
        return f"Welcome to {Pharmacy.pharmacy_name}!"

    @classmethod
    def add_available_medicine(cls, name, quantity, price, expiration_date):
        cls.available_medicines.append(Pharmacy(name, quantity, price, expiration_date))

    @classmethod
    def sell_medicine(cls, name):
        for medicine in cls.available_medicines:
            if medicine.name == name:
                if medicine.quantity > 0:
                    medicine.quantity -= 1
                    cls.sold_medicines.append(medicine)
                    if medicine.quantity == 0:
                        cls.available_medicines.pop(cls.available_medicines.index(medicine))
                else:
                    return "Medicine out of stock"
                return
        return "Medicine not available"

    @classmethod
    def add_needed_medicine(cls, name):
        cls.needed_medicines.append(name)

    @classmethod
    def list_available(cls):
        return "Available Medicines:\n" + "\n".join(
            [f"Name: {medicine.name}, Quantity: {medicine.quantity}, Price: ${medicine.price}, Expiration Date: {medicine.expiration_date}" 
            for medicine in cls.available_medicines])

    @classmethod
    def list_sold(cls):
        return "Sold Medicines:\n" + "\n".join(
            [f"Name: {medicine.name}, Quantity: {medicine.quantity}, Price: ${medicine.price}, Expiration Date: {medicine.expiration_date}" 
            for medicine in cls.sold_medicines])

    @classmethod
    def list_needed(cls):
        return f"Needed Medicines: {', '.join(cls.needed_medicines)}"

# إنشاء كائن من الكلاس
pharmacy = Pharmacy

# إضافة أدوية إلى القائمة المتاحة
Pharmacy.add_available_medicine("Paracetamol", 10, 2.5, "2025-12-31")
Pharmacy.add_available_medicine("Aspirin", 20, 1.5, "2024-06-30")

# إضافة أدوية إلى قائمة الأدوية المطلوبة
Pharmacy.add_needed_medicine("Ibuprofen")

# بيع دواء
Pharmacy.sell_medicine("Paracetamol")

# عرض المعلومات
print(Pharmacy.get_pharmacy_info())
print(Pharmacy.list_available())
print(Pharmacy.list_sold())
print(Pharmacy.list_needed())
