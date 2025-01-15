# Resume Pre-Screener using OpenAI

A fun python script that takes in a persons details, made up, and decides whether to call this person forward for interview. 
The candidate is fictitious.

A Python script uses PyPDF2 to process pdfs, extract text, to build a profile for the candidate, for OpenAI to make a determination.

Using the inputs provided (PDFs) , OpenAI will make a determination,using prompt information, whether to call eligible candidates forward for interview.

## Features

- Extracts text from PDF documents: cv, police clearances, and driving declarations.
- Compares candidate details against a job description and analysis criteria.
- Uses OpenAI api to get detailed feedback.

### Response

Running the program several times will produce different responses. Sometimes John, the same candidate, gets the call, sometimes he does not.

This variability is due to the probabilistic nature of the AI model: slight variations in input interpretation or randomness in the model's outputs etc.

The user however may make their own decision and agree or override the model decision. 





## Prompt

The prompt used is designed to evaluate the content and structure of a CV and relevance.
It assesses whether the CV aligns with the job description.


|               | Comment                                                            |
|---------------|--------------------------------------------------------------------|
| Role/ persona | You are a recruitment expert                                       |
| Response      | concise and clear                                                  |
| Task          | analyse and report                                                 |
| Output        | how the output is to be presented                                  |
| Consideration | CTA for UK and Ireland candidates<br/>make Yes or No for interview |
| Choice        | Present the OpenAI choice                                          |



## Profile Candidate Information

- CV
- Police Clearance
- Driving declaration

## Job Description
 
The job description is supplies as an input file - job_description.txt 
The file can be modified as required, depending on the job requirements.

## Example Run


```
************************************************************

Resume Analysis: 
 Call for interview: YES

**Job Posting:**

- Java analyst programmer required.
- Onsite in Dublin, with travel to client sites.
- Must have leadership skills.
- 5 Years or more Java experience.
- Analysis and AI skills desirable.
- Clean driving licence required for client site visits.
- 3rd level education desirable.

**Information Gap:**
- No mention of analysis and AI skills.
- Specific details about eligibility to work in Ireland.
  
**Detailed Decision:**
1. **Skill Alignment:**
   - John Smith has over 15 years of Java experience, surpassing the 5-year requirement.
   - Leadership skills are evident from his experience in leading a team and mentoring junior developers.
   - No explicit mention of analysis and AI skills.

2. **Keyword Matching:**
   - The resume aligns well with the job description keywords such as Java, leadership, software lifecycle, and mentoring.
   - Suggested keywords to add: "AI", "data analysis".

3. **CV Recommendations:**
   - Highlight any exposure to AI projects or data analysis explicitly, if applicable.
   - Ensure to discuss eligibility to work in Ireland considering his current UK residence.
   - Adding more client-related travel experiences, if any, could strengthen the application.

4. **Alignment Score:**
   - 9/10. The resume aligns closely with the job requirements, with minor gaps in analysis and AI expertise.

5. **Years in Leadership:**
   - Approximately 5 years, considering roles involving leading and mentoring in recent positions.

6. **Education:**
   - Holds a BSc (Hons) in Computer Science, which meets the desirable education requirement.

7. **Certificates:**
   - Oracle Certified Professional, Java SE.
   - Scrum Master Certification.

8. **Driving Licence:**
   - Full UK driving license with 2 penalty points, meets the requirement to drive for client site visits.

9. **Eligibility to Work in Ireland:**
   - As a UK national, eligible to work in Ireland under the Common Travel Area agreement.

10. **Police Background Check:**
    - No criminal record.

John Smith is a strong candidate for the role based on his extensive Java experience and leadership skills. Invitations to clarify any analysis or AI experience during the interview and discuss his eligibility to work onsite in Dublin are recommended.


```


## Prerequisites

Python 3.x installed.
An OpenAI API key (stored securely in a .env file).

## Clone the repo

git clone https://github.com/your-username/OpenAI_Resume_Screener.git
pip install -r requirements.txt
Add your OpenAI API key to a .env file
python main.py
