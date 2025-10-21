import google.generativeai as genai

gemini_model = "gemini-2.0-flash"

def summarize_news(api_key, text):

    # set API key
    genai.configure(api_key=api_key)

    # Choose Model
    model = genai.GenerativeModel(gemini_model)

    # Create Prompt
    #prompt = f"สรุปข่าวเทคโนโลยีนี้ให้เข้าใจง่ายภายใน 3 บรรทัด:\n{text}"

    prompt = f"""
        คุณคือนักวิเคราะห์ข่าวเทคโนโลยีชื่อ TungTungSama
        หน้าที่ของคุณคือสรุปข่าวเทคโนโลยีจากข้อความที่ได้รับให้สั้น กระชับ และเข้าใจง่าย
        เขียนในโทนเป็นมิตรแต่ดูฉลาด มีความรู้
        พูดในสไตล์ของ TungTungSama — ฉลาด มั่นใจ แต่มีอารมณ์ขันเล็กน้อย เช่น “เทคโนโลยีไม่หยุดพัฒนาจริงๆ!”

        สรุปประเด็นสำคัญของข่าวนี้ใน 3-5 บรรทัด
        อย่าใส่คำขอโทษหรือพูดว่าขาดข้อมูล จงสรุปจากสิ่งที่มีเท่านั้น

        ข่าว:
        {text}
    """

    # Send Prompt
    response = model.generate_content(prompt)
    response_text = response.text.strip() # Remove unnecessarily whitespace and characters

    return response_text