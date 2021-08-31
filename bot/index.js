const { Client } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const fs = require("fs");

const SESSION_FILE_PATH = "./session.json";

let client;
let session_data;

const initWithSession = () => {
  console.log("Validando sesion con whatsapp..");
  session_data = require(SESSION_FILE_PATH);
  client = new Client({
    session: session_data,
  });

  client.on("ready", () => {
    console.log("El cliente esta listo.");
    listenMessage();
  });

  client.on("auth_failure", () => {
    console.log("Error con la autentificacion");
  });

  client.initialize();
};

const initWithoutSession = () => {
  console.log("Iniciando una nueva sesion..");
  client = new Client();

  client.on("qr", (qr) => {
    qrcode.generate(qr, { small: true });
  });

  client.on("ready", () => {
    console.log("Listo");
    connectionReady();
  });

  client.on("auth_failure", () => {
    console.log("Error con la autentificacion");
  });

  client.on("authenticated", (session) => {
    session_data = session;
    fs.writeFile(SESSION_FILE_PATH, JSON.stringify(session), (err) => {
      if (err) console.log(err);
    });
  });

  client.initialize();
};

const listenMessage = () => {
  client.on("message", async (msg) => {
    const { from, to, body } = msg;
    sendMessage(from, "¡Hola soy Codavi!\nEstoy todavía en desarrollo 🕦");
  });
};

const sendMessage = (to, text) => {
  client.sendMessage(to, text);
};

fs.existsSync(SESSION_FILE_PATH) ? initWithSession() : initWithoutSession();
