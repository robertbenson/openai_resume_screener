import os
import PyPDF2
from openai import OpenAI


def read_file(file_path: str, description: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {description} file '{file_path}' not found.")
        return ""

def read_all_pdfs(directory: str) -> str:
    """
    Reads all .pdf files in the given directory. Extracts text from
    and concatenates into one string.
    Returns the combined text for all PDFs.
    """
    all_pdf_text = []

    # Loop through the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            try:
                with open(pdf_path, 'rb') as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    file_text = []

                    # Extract text from each page of this PDF
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            file_text.append(page_text)

                    # Combine the pages for this single PDF
                    pdf_text = "\n".join(file_text)
                    # Append a heading so you know which PDF text came from
                    all_pdf_text.append(
                        f"--- Contents of {filename} ---\n{pdf_text}")
            except Exception as e:
                print(f"Error reading {pdf_path}: {e}")

    # Combine all PDFs' text
    return "\n\n".join(all_pdf_text)


def read_analysis_criteria():
    """
    Reads the analysis criteria from a file called 'analysis_criteria.txt'
    and returns its content as a string.
    """
    with open("analysis_criteria.txt", "r", encoding="utf-8") as file:
        analysis_criteria = file.read()
    return analysis_criteria

def read_job_description():
    """
    Reads the job_description from a file called 'job_description.txt'
    and returns its content as a string.
    """
    try:
        with open("job_description.txt", "r", encoding="utf-8") as file:
            job_description = file.read()
        return job_description
    except FileNotFoundError:
        print("Error: 'job_description.txt' not found.")
        return None


def messages_for(system_prompt_input, user_prompt_input):
    return [
        {"role": "system", "content": system_prompt_input},
        {"role": "user", "content": user_prompt_input}
    ]


def main():
    openai = OpenAI()

    # Read all PDF files from the 'PDF' directory
    cv_text = read_all_pdfs("PDF")

    system_prompt = """You are a job recruitment expert. 
    You will assist with resume analysis. 
    Provide responses that are concise, clear, and to the point. 
    Your task is to analyse a resume against a given job posting and provide feedback on how well the resume aligns with the job requirements. 
    The first line of the analysis should stated clearly "Call for interview: " yes or no , for call for interview. If no, write in upper case with a short summary of why not.
    The response should be in 3 parts: The first part will be the job posting, do not embellish, the second part will be the information gap, where information was requested but not supplied.
    Take into consideration the Common Travel Area agreement between Ireland and the UK regarding the visa requirements. 
    The third part will be a detailed decision, determined by the analysis criteria as to whether to call for interview.

    """

    criteria = read_file("analysis_criteria.txt", "Analysis Criteria")
    # print("Bob's Criteria:\n", criteria)

    job_description = read_file("job_description.txt", "Job Description")
    # print("Job Description:\n\n", job_description)

    # construct the user prompt

    user_prompt = "Job Posting:"
    user_prompt += job_description
    user_prompt += "analysis criteria:"
    user_prompt += criteria
    user_prompt += "CV"
    user_prompt += cv_text

    # call OpenAI's ChatCompletion endpoint
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages_for(system_prompt, user_prompt)
    )

    # print the response

    print()
    print('*' * 60)
    print("\nResume Analysis: \n",response.choices[0].message.content)



if __name__ == "__main__":
    main()
