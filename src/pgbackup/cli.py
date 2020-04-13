from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination= values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Back up Postgresql databases locally or to AWL S3
    """)

    parser.add_argument("url", help="URL of the database to backup")
    parser.add_argument("--driver",
            help="hot and where to store backup",
            nargs=2,
            action=DriverAction,
            required=True)

    return parser
