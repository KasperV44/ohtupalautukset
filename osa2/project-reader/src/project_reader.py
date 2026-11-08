from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_data = toml.loads(content)

        name = ""
        description = ""
        license_val = ""
        authors_list = []
        dependencies = []
        dev_dependencies = []

        # 1. Haetaan projektin perustiedot [project]-osiosta
        if "project" in toml_data:
            proj = toml_data["project"]
            name = proj.get("name", "")
            description = proj.get("description", "")
            license_val = proj.get("license", "")
            
            # Tekijät voivat olla sanakirjoja tai merkkijonoja
            raw_authors = proj.get("authors", [])
            for author in raw_authors:
                if isinstance(author, dict) and "name" in author:
                    authors_list.append(author["name"])
                elif isinstance(author, str):
                    authors_list.append(author)

            # Jos requires-python on olemassa, lisätään "python" ensimmäiseksi riippuvuudeksi
            requires_python = proj.get("requires-python", "")
            if requires_python:
                dependencies.append("python")

            # Tuotantoriippuvuudet (poistetaan versioehdot pois nimenä esittämistä varten)
            raw_deps = proj.get("dependencies", [])
            for d in raw_deps:
                for op in [">=", "==", "<=", ">", "<", "~="]:
                    if op in d:
                        d = d.split(op)[0]
                        break
                d_name = d.strip()
                if d_name.lower() != "python":
                    dependencies.append(d_name)

        # 2. Haetaan kehitysaikaiset riippuvuudet ([dependency-groups])
        raw_dev_deps = []
        if "dependency-groups" in toml_data:
            dep_groups = toml_data["dependency-groups"]
            for key in ["dev", "development", "test"]:
                if key in dep_groups:
                    raw_dev_deps = dep_groups[key]
                    break

        for d in raw_dev_deps:
            if isinstance(d, str):
                for op in [">=", "==", "<=", ">", "<", "~="]:
                    if op in d:
                        d = d.split(op)[0]
                        break
                dev_dependencies.append(d.strip())
            else:
                dev_dependencies.append(str(d))

        return Project(name, description, dependencies, dev_dependencies, license_val, authors_list)
