import { Box } from "@mui/material";
import { DesktopCard } from "./Card";

import StationaryImage from "../../assets/pages/desktop/stationary_500.jpg";
import DrinksImage from "../../assets/pages/desktop/drinks_500.jpg";
import TechImage from "../../assets/pages/desktop/tech_500.jpg";

export function DesktopOverview({ topics }) {
    return (
        <Box
            sx={{
                display: "flex",
                flexDirection: "row",
                flexWrap: "wrap",
                gap: "20px",
                justifyContent: "center",
            }}
        >
            <DesktopCard
                img={StationaryImage}
                alt="stationary"
                title="Канцелярия"
                description="Здесь можно сообщить администратору, что у вас закончились ручки или чистые листы бумаги"
                href="/stationary"
            />
            <DesktopCard
                img={DrinksImage}
                alt="drinks"
                title="Напитки"
                description="Позволяет планировать и заказывать приготовление кофе, чая, охлаждающих напитков"
                href="/drinks"
            />
            <DesktopCard
                img={TechImage}
                alt="tech"
                title="Техника"
                description="Здесь можно заказать недостающую канцелярию"
                href="/tech"
            />
        </Box>
    );
}
