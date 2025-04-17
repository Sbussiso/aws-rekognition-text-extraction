# Image Text Extractor

This project is a Python script that uses Amazon Rekognition to extract text from images. It takes an image URL as input, downloads the image, and sends it to the Rekognition service for text detection. The extracted text is then printed to the console.

## Introduction

The Image Text Extractor is a useful tool for extracting text from images, which can be beneficial in various scenarios, such as:

- Digitizing text from scanned documents or images
- Extracting text from product labels or packaging
- Analyzing text in images for data mining or research purposes

The script leverages the power of Amazon Rekognition, a computer vision service provided by Amazon Web Services (AWS), to perform accurate text detection and extraction.

## Prerequisites

Before running the Image Text Extractor, ensure that you have the following prerequisites installed:

- Python 3.x
- AWS account with appropriate permissions to use Amazon Rekognition
- AWS credentials (Access Key ID and Secret Access Key)

## Installation

1. Clone the repository or download the source code.
2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On Unix or macOS:

   ```bash
   source venv/bin/activate
   ```

4. Install the required Python packages:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root directory and add your AWS credentials:

```
AWS_ACCESS_KEY=your_access_key_id
AWS_SECRET_KEY=your_secret_access_key
AWS_REGION=your_aws_region
```

Replace `your_access_key_id`, `your_secret_access_key`, and `your_aws_region` with your actual AWS credentials and the desired AWS region.

## Usage

1. Run the script:

```bash
python main.py
```

2. When prompted, enter the URL of the image you want to extract text from.

3. The script will download the image, send it to Amazon Rekognition for text detection, and print the extracted text to the console.

## Contributing

Contributions to the Image Text Extractor project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

When contributing, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.
2. Make your changes and ensure that the code follows best practices and is well-documented.
3. Test your changes thoroughly.
4. Submit a pull request with a clear description of your changes and their purpose.

## License

This project is licensed under the [MIT License](LICENSE).