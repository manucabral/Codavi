import styled from "styled-components";
import Card from "../components/Card";

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function Home({ vacunas }) {
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
            title="Comparativa por vacunas"
            description="Cantidad vacunas aplicadas por marca solamente la primera dosis."
            data={Object.values(vacunas["comparativaVacunas"])}
          />
        </Content>
      </Subcontainer>
    </Main>
  );
}

export async function getStaticProps(context) {
  const res = await fetch(`https://codavi.herokuapp.com/covid`);
  const vacunas = await res.json();

  if (!vacunas) {
    return {
      redirect: {
        destination: "/",
        permanent: vacunas,
      },
    };
  }

  return {
    props: { vacunas },
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
