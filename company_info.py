def get_company_info(company):
    data = {
        "Google": "Innovative global tech company with strong benefits",
        "TCS": "Stable IT services company with job security",
        "Infosys": "Corporate IT firm with strong training culture"
    }

    return data.get(company, "No company data available")