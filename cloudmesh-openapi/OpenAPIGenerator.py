import textwrap
class OpenaAPIGenerator:
    openAPITemplate = """
    openapi: 3.0.0
    info:
      title: {title}
      description: {description}
      version: {version}
    servers:
      - url: http://localhost/cloudmesh/{title}
        description: Optional server description, e.g. Main (production) server
    paths:
      /{name}:
         get:
             parameters:
               {parameters} 
    """

    def sampleFunction(x: int, y: float) -> float:
        """
        addNumber sample.
        :param x: x value
        :type x: int
        :param y: y value
        :type y: float
        :return: result
        :return type: int
        """
        return x + y

    functionName = sampleFunction

    def generate_parameter(self, name, _type, description):
        """ function to generate parameters YAMAL contents"""
        spec = textwrap.indent(f"""
               - in: query
                 name: {name}
                 schema:
                   type: {_type}
                 description: {description} """, "")
        return spec

    def generate_openapi(self, write=True):
        """ function to generate open API of python function."""
        f = self.functionName
        description = f.__doc__.strip().split("\n")[0]
        version = open('VERSION', 'r').read()
        title = f.__name__
        parameters = self.populateParameters()
        spec = self.openAPITemplate.format(
            title=title,
            name=f.__name__,
            description=description,
            version=version,
            parameters=parameters.strip(),
        )
        if write:
            version = open(f"{title}.yaml", 'w').write(spec)
        return spec

    def populateParameters(self):
        """ Function to loop all the parameters of given function and generate specification"""
        spec = str()
        for parameter, _type in self.functionName.__annotations__.items():
            if parameter == "return":
                break
            if _type == int:
                _type = 'integer'
            elif _type == bool:
                _type = 'boolean'
            elif _type == float:
                _type = 'float'
            else:
                _type = 'unkown'
            spec = spec + self.generate_parameter(parameter, _type, "not yet available, you can read it from docstring")
        return spec


if __name__ == "__main__":
    openAPI = OpenaAPIGenerator()
    spec = openAPI.generate_openapi()
