import styled from "styled-components";
import Card from "../components/Card";

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function Home({ vacunas, gpd, gsd }) {
  return (
    <Main>
      <Container>
        <Title>CODAVI</Title>
        <Description>
          Visualización y estadísticas sobre el COVID-19 en toda la Argentina.
        </Description>
      </Container>
      <Subcontainer>
        <Content>
          <Card
            title={vacunas["titulo"]}
            description={vacunas["descripcion"]}
            data={Object.values(vacunas["data"])}
          />
        </Content>
        <Content>
          <Card
            title={gpd["titulo"]}
            description={
              gpd["status"] === 200 ? gpd["descripcion"] : gpd["data"]
            }
            data={gpd["status"] === 200 ? Object.values(gpd["data"]) : []}
          />
          <Card
            title={gsd["titulo"]}
            description={
              gsd["status"] === 200 ? gsd["descripcion"] : gsd["data"]
            }
            data={gsd["status"] === 200 ? Object.values(gsd["data"]) : []}
          />
        </Content>
      </Subcontainer>
      <Container>
        <Description>&copy; Copyright 2021 - Manuel Cabral</Description>
      </Container>
    </Main>
  );
}

export async function getStaticProps(context) {
  const res = await fetch(`https://codavi.herokuapp.com/vacunas`);
  const resgpd = await fetch(`https://codavi.herokuapp.com/genero/1`);
  const resgsd = await fetch(`https://codavi.herokuapp.com/genero/2`);
  const gpd = await resgpd.json();
  const gsd = await resgsd.json();
  const vacunas = await res.json();

  if (!vacunas)
    return {
      redirect: {
        destination: "/",
        permanent: vacunas,
      },
    };

  if (!gpd)
    return {
      redirect: {
        destination: "/",
        permanent: gpd,
      },
    };

  if (!gsd)
    return {
      redirect: {
        destination: "/",
        permanent: gsd,
      },
    };

  return {
    props: { vacunas, gpd, gsd },
  };
}

const Main = styled.div`
  text-align: center;
  position: absolute;
  width: 100%;
  height: 100vh;
  background-color: ${({ theme }) => theme.backgrounds.primary};
`;

const Container = styled.div`
  display: flex;
  padding: 1rem;

  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: ${({ theme }) => theme.backgrounds.secondary};
`;

const Subcontainer = styled.div`
  display: flex;
  padding: 1rem;
  padding-bottom: 4rem;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: ${({ theme }) => theme.backgrounds.primary};
`;

const Title = styled.h1`
  font-size: 64px;
  color: #e80000;
`;

const Description = styled.p`
  color: ${({ theme }) => theme.colors.secondary};
`;

const Content = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding-top: 1rem;
  justify-content: space-around;

  @media screen and (max-width: 720px) {
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;
  }
`;
