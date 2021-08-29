import useSwr from "swr";
import styled from "styled-components";

const fetcher = (url) => fetch(url).then((res) => res.json());

const Main = styled.div`
  text-align: center;
  position: absolute;
  width: 100%;
  height: 100vh;
  background-color: ${({ theme }) => theme.backgrounds.primary};
`;

const Content = styled.div`
  display: flex;
  padding: 1rem;

  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: ${({ theme }) => theme.backgrounds.secondary};
`;

const Title = styled.h1`
  font-size: 64px;
  color: #e80000;
`;

const Subtitle = styled.h2`
  color: ${({ theme }) => theme.colors.primary};
`;

const Description = styled.p`
  color: ${({ theme }) => theme.colors.secondary};
`;

const ContentStats = styled.p`
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

const Item = styled.p`
  padding: 1rem;
  &:hover {
    cursor: pointer;
    background-color: ${({ theme }) => theme.backgrounds.secondary};
  }
  //border: 2px solid #e80000;
`;

export default function Home() {
  const { data, error } = useSwr("/api/covid", fetcher);

  if (error) return <Title>Error al cargar.</Title>;
  if (!data) return <Title>Cargando..</Title>;

  return (
    <Main>
      <Content>
        <Title>CODAVI</Title>
        <Description>
          Visualización y estadísticas sobre el COVID-19 en toda la Argentina.
        </Description>
      </Content>
      <ContentStats>
        <Item>
          <Subtitle>Mujeres vs Hombres</Subtitle>
          <Description>
            Cantidad de vacunados por género solamente en la primera dosis.
          </Description>
        </Item>
        <Item>
          <Subtitle>Comparativa de vacunas</Subtitle>
          <Description>
            Cantidad aplicada de cada vacuna (marca) en la primera dosis.
          </Description>
          <Title>54950</Title>
        </Item>
      </ContentStats>
    </Main>
  );
}
