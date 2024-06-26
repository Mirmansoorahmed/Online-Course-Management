# Online Course Management System

Welcome to the Online Course Management System! This system allows teachers to manage courses and students, and students to interact with available courses.

## Table of Contents

1. [Getting Started](#getting-started)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Deployment on AWS](#deployment-on-aws)
6. [Port Configuration](#port-configuration)
7. [Contributing](#contributing)
8. [License](#license)

## Getting Started

To get started with the Online Course Management System, follow the installation instructions below.

## System Requirements

- Python 3.x
- Docker
- AWS Account (for deployment)

## Installation

## Clone the repository:
  git clone https://github.com/your-username/online-course-management-system.git
  cd online-course-management-system

## Install dependencies:
  pip install -r requirements.txt

## Run the application locally:
  streamlit run app.py

Access the application in your web browser at `http://localhost:8501`.

## Deployment on AWS

1. Set up an AWS account if you haven't already.
2. Containerize the application using Docker:
docker build -t online-course-management .

4. Push the Docker image to a container registry (e.g., Amazon ECR).
5. Configure AWS ECS (Elastic Container Service) clusters, services, and task definitions.
6. Deploy the Docker containers to ECS.
7. Access the deployed application using the ECS public DNS or load balancer URL.

For detailed instructions on AWS ECS deployment, refer to the [AWS ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

## Port Configuration

The application runs on port 8501 by default. Ensure that port 8501 is accessible and not blocked by firewalls or other applications.
## Testing
pip install pytest

Run in this project directory

python -m pytest  unit_tests.py

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).

