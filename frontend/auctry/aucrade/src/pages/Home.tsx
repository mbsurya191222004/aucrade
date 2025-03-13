import { useState } from "react";
import { AllItems } from "../API/api";

export const Home = () => {
  const [items, SetItems] = useState();

  const handleClick = (e: any) => {
    e.preventDefault();
    const response = AllItems();
    response
      .then((data) => {
        SetItems(data);
      })
      .catch((error) => console.error(error));
  };

  return (
    <>
      <button onClick={(e) => handleClick(e)}> hhhh</button>
      <div>{JSON.stringify(items)}</div>
    </>
  );
};
