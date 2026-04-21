from enum import Enum

class ServiceType(str, Enum):
    residential_lending = "Residential Lending"
    commercial_lending = "Commercial Lending"
    smsf_lending = "SMSF Lending"
    asset_finance_lending = "Asset Finance Lending"
    private_funding = "Private Funding"
    business_operations_accounting = "Business Operations & Accounting"
    other = "Other / Not Sure"
