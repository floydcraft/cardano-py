const http = require('http');
const os = require('os');
const express = require('express');
const multiaddr = require('multiaddr');

const server_addr = multiaddr("/ip4/0.0.0.0/tcp/8080");

var app = express();

app.get('/', function (req, res) {
    res.redirect('https://github.com/floydcraft/cardano-py');
});

app.get('/api/stakepool/metadata', function (req, res) {
    let data = {
        "name": "CardanoPy🥧",
        "description": "pip3 install --upgrade cardanopy # Cardano python3 CLI -> profit!",
        "ticker": "₳Py🥧",
        "homepage": "https://cardanopy.com"
    }
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(data));
});

app.listen(server_addr.nodeAddress().port, server_addr.nodeAddress().address, () => {
  console.log(`Server running at http://${server_addr.nodeAddress().address}:${server_addr.nodeAddress().port}/`);
});

