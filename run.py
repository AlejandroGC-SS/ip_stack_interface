from arguments import Arguments
from environment_variables import EnvironmentVariables
from ip_stack import IpStack


def main() -> None:
    arguments = Arguments()
    env = EnvironmentVariables()
    ip_stack = IpStack(env.ip_stack_api_token,env.api_stack_base_url)
    latitude, longitude = ip_stack.get_ip_location(arguments.ip_address)

    print(f"latitude : {latitude}")
    print(f"longitude: {longitude}")


if __name__ == "__main__":
    main()
