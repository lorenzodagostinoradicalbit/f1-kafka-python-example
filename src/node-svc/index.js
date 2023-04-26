const { default: axios } = require("axios");
const express = require("express")
const app = express()

const flaskSvc = process.env.FLASK_SVC
const port = process.env.PORT

app.get('/', (req, res) => {
    res.json({"message": "ok"});
});

app.get('/data', async (req, res) => {
    const flaskResp = await axios.get(`${flaskSvc}/`)
    res.json(flaskResp.data);
});

app.get('/start', async (req, res) => {
    const flaskResp = await axios.get(`${flaskSvc}/start`);
    res.json(flaskResp.data);
});

app.get('/stop', async (req, res) => {
    const flaskResp = await axios.get(`${flaskSvc}/stop`);
    res.json(flaskResp.data);
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});