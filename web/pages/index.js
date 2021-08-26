import Link from "next/link";
export default function Inicio() {
  return (
    <div>
      <div>Codavi</div>
      <Link href="/info" as={process.env.BACKEND_URL + "/info"}>
        <a>Sobre el proyecto</a>
      </Link>
    </div>
  );
}
