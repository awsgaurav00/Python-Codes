import pandas as pd
import numpy as np

class WebDevCostAnalyzer:
    def __init__(self):
        """
        Initialize the cost analysis tool for web development projects
        """
        self.cost_categories = {
            'design': 0,
            'frontend_development': 0,
            'backend_development': 0,
            'database': 0,
            'hosting': 0,
            'third_party_services': 0,
            'testing': 0,
            'project_management': 0,
            'maintenance': 0
        }
        self.hourly_rates = {
            'junior_developer': 50,
            'mid_level_developer': 100,
            'senior_developer': 150,
            'designer': 75,
            'project_manager': 125
        }

    def add_labor_cost(self, category, role, hours):
        """
        Calculate labor cost for a specific project category

        :param category: Development category (e.g., 'frontend_development')
        :param role: Developer role (e.g., 'senior_developer')
        :param hours: Number of hours worked
        """
        if category not in self.cost_categories:
            raise ValueError(f"Invalid category: {category}")

        if role not in self.hourly_rates:
            raise ValueError(f"Invalid role: {role}")

        labor_cost = self.hourly_rates[role] * hours
        self.cost_categories[category] += labor_cost

    def add_fixed_cost(self, category, amount):
        """
        Add fixed costs like hosting, third-party services

        :param category: Cost category
        :param amount: Fixed cost amount
        """
        if category not in self.cost_categories:
            raise ValueError(f"Invalid category: {category}")

        self.cost_categories[category] += amount

    def calculate_total_cost(self):
        """
        Calculate total project cost and provide detailed breakdown

        :return: Dictionary with total cost and cost breakdown
        """
        total_cost = sum(self.cost_categories.values())

        # Calculate percentage of total for each category
        cost_percentages = {
            category: (cost / total_cost * 100) 
            for category, cost in self.cost_categories.items()
        }

        return {
            'total_cost': total_cost,
            'cost_breakdown': self.cost_categories,
            'cost_percentages': cost_percentages
        }

    def estimate_maintenance_cost(self, annual_maintenance_percentage=0.2):
        """
        Estimate annual maintenance cost

        :param annual_maintenance_percentage: Percentage of total project cost for annual maintenance
        :return: Estimated annual maintenance cost
        """
        total_cost = sum(self.cost_categories.values())
        maintenance_cost = total_cost * annual_maintenance_percentage
        self.cost_categories['maintenance'] = maintenance_cost
        return maintenance_cost

def example_web_project_cost_analysis():
    """
    Example usage of WebDevCostAnalyzer
    """
    project = WebDevCostAnalyzer()

    # Frontend Development
    project.add_labor_cost('frontend_development', 'mid_level_developer', 120)
    project.add_labor_cost('frontend_development', 'senior_developer', 80)

    # Backend Development
    project.add_labor_cost('backend_development', 'senior_developer', 160)

    # Design
    project.add_labor_cost('design', 'designer', 40)

    # Fixed Costs
    project.add_fixed_cost('hosting', 1200)  # Annual hosting cost
    project.add_fixed_cost('third_party_services', 600)  # Annual services

    # Project Management
    project.add_labor_cost('project_management', 'project_manager', 50)

    # Calculate Results
    results = project.calculate_total_cost()
    print("Total Project Cost: ${:,.2f}".format(results['total_cost']))
    print("\nCost Breakdown:")
    for category, cost in results['cost_breakdown'].items():
        print(f"{category.replace('_', ' ').title()}: ${cost:,.2f}")

    print("\nCost Percentages:")
    for category, percentage in results['cost_percentages'].items():
        print(f"{category.replace('_', ' ').title()}: {percentage:.2f}%")

    # Estimate Maintenance
    annual_maintenance = project.estimate_maintenance_cost()
    print(f"\nEstimated Annual Maintenance Cost: ${annual_maintenance:,.2f}")

# Uncomment to run the example
example_web_project_cost_analysis()