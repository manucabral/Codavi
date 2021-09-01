const { Client } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const fs = require("fs");
const fetch = require("node-fetch");
let menu = 0;
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
  client.on("message_create", async (msg) => {
    const { from, to, body } = msg;
    var opt = body
    console.log(body)
    if (opt === "Codavi") {
      menu = 1
      return sendMessage(to, "¡Hola soy Codavi!\nElegi una vacuna para saber los datos:\n-'Sputnik'\n-'Astrazeneca'\n-'Sinopharm'\n-'Covishield',\n-'Moderna'")
    }
    if (menu === 1){
      console.log("Entro al menu")
      console.log(opt)
      const vaccineInfo = await getVaccineInfo()
      const availableOptions = Object.values(vaccineInfo["comparativaVacunas"]).map(vaccine => {
        return vaccine.subtitle
      })
      if(availableOptions.includes(opt)){
        const vaccine = Object.values(vaccineInfo["comparativaVacunas"]).find(vaccine => {
          return vaccine.subtitle === opt
        })
        sendMessage(to, "Los vacunados con " + opt + " son: " + vaccine.total)
      }
      menu = 0
    }
  });
};

const getVaccineInfo = async () => {
  const res = await fetch(`https://codavi.herokuapp.com/covid`);
  const vacunas = await res.json();
  if (!vacunas) {
    console.log("No se pudieron extraer los datos de las vacunas")
  }
  return vacunas
}

const sendMessage = (to, text) => {
  client.sendMessage(to, text);
};

fs.existsSync(SESSION_FILE_PATH) ? initWithSession() : initWithoutSession();