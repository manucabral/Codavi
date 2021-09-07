const { Client } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const fs = require("fs");
const fetch = require("node-fetch");

let buffer = "";
let SIN_MENU = -1;
let MENU_PRINCIPAL = 0;
let MENU_VACUNAS = 1;
let MENU_GENEROS = 2;

const SESSION_FILE_PATH = "./session.json";

let menu = SIN_MENU;
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
    console.log(msg);
    var opt = body.toLowerCase();

    console.log("> Mensaje recibido: ", opt);

    if (buffer.toLowerCase() === opt) {
      return;
    } else if (menu == MENU_GENEROS) {
      const data = await getGender(opt);
      console.log(data);
      if (data["status"] == "204") {
        sendMessage(
          from,
          "Lo siento 😅\nNo hay datos actualizados para la fecha de hoy."
        );
      } else {
        sendMessage(
          from,
          `Información DOSIS${opt}\nMujeres vacunadas: ${new Intl.NumberFormat().format(
            data["femenino"]
          )}\nHombres vacunados:${new Intl.NumberFormat().format(
            data["masculino"]
          )}\nActualizado el ${data["fecha"]}`
        );
      }
      menu = SIN_MENU;
    } else if (menu == MENU_VACUNAS) {
      const vaccineInfo = await getVaccines();
      const availableOptions = Object.values(vaccineInfo["data"]).map(
        (vaccine) => {
          return vaccine.nombre.toLowerCase();
        }
      );
      if (availableOptions.includes(opt)) {
        const vaccine = Object.values(vaccineInfo["data"]).find((vaccine) => {
          return vaccine.nombre.toLowerCase() === opt;
        });
        sendMessage(
          from,
          "Los vacunados con " + opt + " son: " + vaccine.total
        );
      } else {
        sendMessage(from, "No se encontraron datos de " + opt);
      }
      menu = SIN_MENU;
    } else if (menu === MENU_PRINCIPAL && opt === "1") {
      menu = MENU_VACUNAS;
      return sendMessage(
        from,
        "Elegi una vacuna para saber los datos:\n-Sputnik\n-Astrazeneca\n-Sinopharm\n-Covishield\n-Moderna"
      );
    } else if (menu === MENU_PRINCIPAL && opt === "2") {
      menu = MENU_GENEROS;
      return sendMessage(
        from,
        "¿Qué quieres saber?\n1-Comparativa de géneros primera dosis\n2-Comparativa de géneros segunda dosis"
      );
    } else if (opt === "codavi" && menu === SIN_MENU) {
      menu = MENU_PRINCIPAL;
      return sendMessage(
        from,
        "¡Hola soy Codavi!\n¿En que te puedo ayudar?\n1- Datos sobre vacunas aplicadas\n2- Datos sobre vacunados por género"
      );
    }
  });
};

/**
 * Hace una peticion a la ruta vacunas y gettea los datos
 *
 * @returns Los datos de las vacunas
 */

const getVaccines = async () => {
  const res = await fetch(`https://codavi.herokuapp.com/vacunas`);
  const vacunas = await res.json();
  if (!vacunas) {
    console.log("No se pudieron extraer los datos de las vacunas");
  }
  return vacunas;
};

const getGender = async (dosis) => {
  const res = await fetch(`https://codavi.herokuapp.com/genero/` + dosis);
  const generos = await res.json();
  if (!generos) {
    console.log("No se pudieron extraer los datos de los generos");
  }
  return generos;
};

/**
 * Enviar mensajes del cliente hasta el destinatario
 *
 * @param {*} to Numero destinatario
 * @param {*} text Texto a envi
 */
const sendMessage = (to, text) => {
  console.log("> Enviando:", text);
  buffer = text;
  client.sendMessage(to, text);
};

fs.existsSync(SESSION_FILE_PATH) ? initWithSession() : initWithoutSession();
