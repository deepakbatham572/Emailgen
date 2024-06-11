from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint





def getLLMResponse(form_input,email_sender,email_recipient,email_style ,api_key):
    
   

    llm = HuggingFaceEndpoint(repo_id='mistralai/Mistral-7B-Instruct-v0.2' , huggingfacehub_api_token = api_key)    

    
    
    #Template for building the PROMPT
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    
    """

    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["style","email_topic","sender","recipient"],
    template=template,)

  
    #Generating the response using LLM
    #Last week langchain has recommended to use 'invoke' function for the below please :)
    response=llm.invoke(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))
    print(response)

    return response