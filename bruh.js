import { GoogleGenerativeAI } from "@google/generative-ai";
import dotenv from "dotenv";
dotenv.config();

//configuration

const genAI = new GoogleGenerativeAI(process.env.API_KEY);
const generationConfig = {temperature: 0.9, topP: 1, topK: 1, maxOutputTokens: 4096};

//model

const model = genAI.getGenerativeModel({ model: "gemini-pro", generationConfig});

//content generation

async function generateContent(){ 

    const prompt = "I'm feeling quite tired today.What should I do?";
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    
}

//run

generateContent();
  

