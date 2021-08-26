import Link from "next/link";
export default function NoEncontrado() {
  return (
    <div>
      <div>La pagina que buscas no existe</div>
      <div>
        Volver{" "}
        <Link href="/" as={process.env.BACKEND_URL + "/"}>
          <a>Inicio</a>
        </Link>
      </div>
    </div>
  );
}
