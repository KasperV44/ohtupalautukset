class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license="", authors=None):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors if authors else []

    def __str__(self):
        result = f"Name: {self.name}\nDescription: {self.description}"
        
        if self.license:
            result += f"\nLicense: {self.license}"

        if self.authors:
            result += "\n\nAuthors:"
            for author in self.authors:
                result += f"\n- {author}"

        result += "\n\nDependencies:"
        if self.dependencies:
            for dep in self.dependencies:
                result += f"\n- {dep}"
        else:
            result += "\n-"

        result += "\n\nDevelopment dependencies:"
        if self.dev_dependencies:
            for dep in self.dev_dependencies:
                result += f"\n- {dep}"
        else:
            result += "\n-"

        return result
