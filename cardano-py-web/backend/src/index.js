const os = require('os');
const express = require('express');
const multiaddr = require('multiaddr');
const url = require('url');

const server_addr = multiaddr("/ip4/0.0.0.0/tcp/8080");

var app = express();

app.get('/', function (req, res) {
    const queryObject = url.parse(req.url, true).query;
    console.log(JSON.stringify(queryObject, null, '\t'));
    res.sendFile("index.html", {root: './dist/cardano-py-web'});
});

app.use(express.static('./dist/cardano-py-web'));

app.get('/api/healthcheck', function (req, res) {
    let data = {
        "success": true,
        "cardano_network": process.env.CARDANO_NETWORK
    }
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(data, null, '\t'));
});

app.get('/api/stakepool/metadata', function (req, res) {
    name = "CardanoPy🥧 Testnet"
    if (process.env.CARDANO_NETWORK == "mainnet") {
        name = "CardanoPy🥧"
    }
    let data = {
        "name": name,
        "description": "pip3 install --upgrade cardanopy # Cardano python3 CLI -> Cardano dApp and ETL tools!",
        "ticker": "₳Py🥧",
        "homepage": "https://cardanopy.com/?utm_source=" + process.env.CARDANO_NETWORK + "&utm_medium=metadata&utm_campaign=v1"
    }
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(data, null, '\t'));
});

app.listen(server_addr.nodeAddress().port, server_addr.nodeAddress().address, () => {
  console.log(`Server running at http://${server_addr.nodeAddress().address}:${server_addr.nodeAddress().port}/`);
});

