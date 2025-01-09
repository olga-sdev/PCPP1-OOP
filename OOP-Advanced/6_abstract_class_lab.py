"""
Objectives:
Creation of abstract classes and abstract methods;
multiple inheritance of abstract classes;
overriding abstract methods;
delivering multiple child classes.

Scenario:
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;

create an abstract class representing a scanner that enforces the following methods:
scan_document – returns a string indicating that the document has been scanned;
get_scanner_status – returns information about the scanner (max. resolution, serial number)

Create an abstract class representing a printer that enforces the following methods:
print_document – returns a string indicating that the document has been printed;
get_printer_status – returns information about the printer (max. resolution, serial number)

Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.

Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.
"""

import abc


class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        return 'document has been scanned'

    @abc.abstractmethod
    def get_scanner_status(self, max_resolution, serial_number):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        return 'document has been printed'

    @abc.abstractmethod
    def get_printer_status(self, max_resolution, serial_number):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'


class MFD1(Scanner, Printer):
    def scan_document(self):
        return 'document has been scanned'

    def get_scanner_status(self, max_resolution=70, serial_number=1):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'

    def print_document(self):
        return 'document has been printed'

    def get_printer_status(self, max_resolution=70, serial_number=13):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'


class MFD2(Scanner, Printer):
    def scan_document(self):
        return 'document has been scanned'

    def get_scanner_status(self, max_resolution=700, serial_number=1):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'

    def print_document(self):
        return 'document has been printed'

    def get_printer_status(self, max_resolution=700, serial_number=13):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'

    def printing_operation_history(self):
        return 'operation history was printed'


class MFD3(Scanner, Printer):
    def scan_document(self):
        return 'document has been scanned'

    def get_scanner_status(self, max_resolution=7000, serial_number=3):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'

    def print_document(self):
        return 'document has been printed'

    def get_printer_status(self, max_resolution=7000, serial_number=33):
        return f'max. resolution: {max_resolution}, serial number {serial_number}'

    def printing_operation_history(self):
        return 'operation history was printed'

    def fax_machine(self):
        return 'fax was sent'


mfd1 = MFD1()
print(mfd1.print_document(), mfd1.get_printer_status(), mfd1.scan_document(), mfd1.get_scanner_status())

mfd2 = MFD2()
print(mfd2.print_document(), mfd2.get_printer_status(), mfd2.get_scanner_status(),
      mfd2.scan_document(), mfd2.printing_operation_history())

mfd3 = MFD3()
print(mfd3.print_document(), mfd3.get_printer_status(), mfd3.get_scanner_status(),
      mfd3.scan_document(), mfd3.printing_operation_history(), mfd3.fax_machine())

# document has been printed max. resolution: 70, serial number 13 document has been scanned max. resolution: 70, serial number 1
# document has been printed max. resolution: 700, serial number 13 max. resolution: 700, serial number 1 document has been scanned operation history was printed
# document has been printed max. resolution: 7000, serial number 33 max. resolution: 7000, serial number 3 document has been scanned operation history was printed fax was sent
