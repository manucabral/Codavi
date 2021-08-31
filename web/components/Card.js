import { useState } from "react";
import styled from "styled-components";

const MainCard = styled.div`
  padding: 1rem;
  //border: 2px solid #e80000;
`;

const CardBody = styled.div`
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding-top: 1rem;
  background-color: ${({ theme }) => theme.backgrounds.secondary};
  justify-content: space-around;
`;

const CardBodyItem = styled.div`
  padding: 1rem;
`;

const Title = styled.h1`
  font-size: 28px;
  color: ${({ theme }) => theme.colors.primary};
`;

const Subtitle = styled.h2`
  color: ${({ theme }) => theme.colors.primary};
`;

const Value = styled.h2`
  color: #e80000;
`;

const Description = styled.p`
  color: ${({ theme }) => theme.colors.secondary};
`;

export default function Card({ title, description, data }) {
  var [values] = useState(data);
  return (
    <MainCard>
      <Title>{title}</Title>
      <Description>{description}</Description>
      <CardBody>
        {values.map((e) => (
          <CardBodyItem>
            <Subtitle>{e.subtitle}</Subtitle>
            <Value>{new Intl.NumberFormat().format(e.total)}</Value>
          </CardBodyItem>
        ))}
      </CardBody>
    </MainCard>
  );
}
