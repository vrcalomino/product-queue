import os
import argparse


def create_env_file(folder_path, env_content):
    """Creates an .env file with specified content in the given folder."""

    env_file_path = os.path.join(folder_path, '.env')
    with open(env_file_path, 'w') as env_file:
        env_file.write(env_content)
    print(f".env file created at {env_file_path}")


def parse_key_value_pairs(pairs):
    parsed_args = {}
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            parsed_args[key] = value
        else:
            raise ValueError(f"Invalid argument format: {pair}")
    return parsed_args


def main():
    parser = argparse.ArgumentParser(description="Generate .env files with specified parameters.")
    parser.add_argument('args', nargs='+', help='Arguments in key=value format')
    args = parser.parse_args()

    key_value_pairs = parse_key_value_pairs(args.args)

    RABBITMQ_HOST = key_value_pairs.get('host', "rabbitMQ")
    RABBITMQ_PORT = key_value_pairs.get('port', 5672)
    RABBITMQ_USERNAME = key_value_pairs.get('username', "guest")
    RABBITMQ_PASSWORD = key_value_pairs.get('password', "guest")
    EMAIL_SENDER = key_value_pairs.get('email', "")
    EMAIL_SENDER_PASSWORD = key_value_pairs.get('email_password', "")

    envFilesValues = (
        f'RABBITMQ_HOST={RABBITMQ_HOST}\n'
        f'RABBITMQ_PORT={RABBITMQ_PORT}\n'
        f'RABBITMQ_USERNAME={RABBITMQ_USERNAME}\n'
        f'RABBITMQ_PASSWORD={RABBITMQ_PASSWORD}\n'
        f'EMAIL_SENDER={EMAIL_SENDER}\n'
        f'EMAIL_SENDER_PASSWORD={EMAIL_SENDER_PASSWORD}'
    )

    folders = {
        './product-receiver': envFilesValues,
        './product-request': envFilesValues
    }

    # Create .env files in specified folders
    for folder, content in folders.items():
        create_env_file(folder, content)


if __name__ == "__main__":
    main()

