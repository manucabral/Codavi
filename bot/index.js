const { Client } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const fs = require("fs");

const SESSION_FILE_PATH = "./session.json";

let client;
let session_data;

/**
 * Inicializa el cliente con la sessión registrada.
 */
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

/**
 * Inicializa el cliente con una nueva sesión y genera un código QR.
 */
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

/**
 * Escucha mensajes entrantes.
 */
const listenMessage = () => {
  client.on("message", async (msg) => {
    const { from, to, body } = msg;
    console.log(from, body);
    sendMessage(from, "¡Hola soy Codavi!");
  });
};

/**
 * Envia un mensaje a un usuario.
 *
 * @param {*} to destinatario (identificador)
 * @param {*} text mensaje a enviar
 */
const sendMessage = (to, text) => {
  client.sendMessage(to, text);
};

fs.existsSync(SESSION_FILE_PATH) ? initWithSession() : initWithoutSession();
