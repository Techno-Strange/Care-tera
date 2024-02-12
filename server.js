const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const server = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('care', { reply: null });
});

app.post('/', async (req, res) => {
    const childName = req.body.child_name;
    const childClass = req.body.child_class;
    const childAge = req.body.child_age;
    const prompt = req.body.user_input;

    const apiKey = 'AIzaSyCpyjEPx41lcgmpZfT26tjpJ7eQ2eU0cTY';

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
    };

    const data = {
        messages: [
            { role: 'system', content: 'You are a helpful assistant.' },
            { role: 'user', content: `Child's Name: ${childName}, Class: ${childClass}, Age: ${childAge}, Prompt: ${prompt}` },
        ],
    };

    try {
        const response = await axios.post(apiUrl, data, { headers });
        const reply = response.data.choices[0].message.content;
        res.render('care', { reply });
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});


