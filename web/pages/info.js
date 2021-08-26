import Link from "next/link";
export default function Info() {
  return (
    <div>
      <div>Sobre el proyecto</div>

      <Link href="/" as={process.env.BACKEND_URL + "/"}>
        <a>Volver al inicio</a>
      </Link>
    </div>
  );
}
