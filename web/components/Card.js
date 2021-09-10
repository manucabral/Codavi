import { useState } from "react";
import styled from "styled-components";

const MainCard = styled.div`
  margin: 1rem;
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(255, 0, 0, 0.5);
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
`;

const CardBody = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  background-color: ${({ theme }) => theme.backgrounds.secondary};
  justify-content: space-around;
`;

const CardHead = styled.div`
  background-color: ${({ theme }) => theme.backgrounds.tertiary};
`;

const CardBodyColumn = styled.div`
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  background-color: ${({ theme }) => theme.backgrounds.secondary};
`;

const CardBodyItem = styled.div``;

const Title = styled.h1`
  padding: 1rem;
  font-size: 28px;
  color: ${({ theme }) => theme.colors.secondary};
`;

const Subtitle = styled.h2`
  padding-left: 1rem;
  padding-right: 1rem;
  color: ${({ theme }) => theme.colors.tertiary};
`;

const Value = styled.h2`
  color: ${({ theme }) => theme.colors.second_main};
`;

const Description = styled.p`
  color: ${({ theme }) => theme.colors.tertiary};
`;

export default function Card({ title, description, data, column }) {
  var [values] = useState(data);
  console.log(values);
  return (
    <MainCard>
      <CardHead>
        <Title>{title}</Title>
        <Description>{description}</Description>
      </CardHead>
      {column ? (
        <CardBodyColumn>
          {values.map((e, index) => (
            <CardBodyItem key={index}>
              <Subtitle>{e.nombre}</Subtitle>
              <Value>{new Intl.NumberFormat().format(e.total)}</Value>
            </CardBodyItem>
          ))}
        </CardBodyColumn>
      ) : (
        <CardBody>
          {values.map((e, index) => (
            <CardBodyItem key={index}>
              <Subtitle>{e.nombre}</Subtitle>
              <Value>{new Intl.NumberFormat().format(e.total)}</Value>
            </CardBodyItem>
          ))}
        </CardBody>
      )}
    </MainCard>
  );
}
