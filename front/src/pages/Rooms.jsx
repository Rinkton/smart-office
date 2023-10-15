import { Box, Typography } from "@mui/material";

import { RoomCard } from "../components/rooms/Card";

import Room1 from "../assets/pages/meeting_rooms/1_500.jpg";
import Room2 from "../assets/pages/meeting_rooms/2_500.jpg";
import Room3 from "../assets/pages/meeting_rooms/3_500.jpg";
import Room4 from "../assets/pages/meeting_rooms/4_500.jpg";
import Room5 from "../assets/pages/meeting_rooms/5_500.jpg";

export function MeetingRooms() {
    return (
        <>
            <Typography
                variant="h6"
                style={{
                    padding: "10px 10px 30px 30px",
                    textAlign: "start",
                }}
            >
                Переговорные
            </Typography>
                <Box
                    sx={{
                        display: "flex",
                        flexDirection: "column",
                        gap: "20px",
                        paddingLeft: "30px",
                    }}
                >
                    <RoomCard
                        img={Room1}
                        alt="Хипстерский Хаб"
                        title="Хипстерский Хаб"
                        description="9 мест"
                    />
                    <RoomCard
                        img={Room2}
                        alt="Творческая Коммуна"
                        title="Творческая Коммуна"
                        description="15 мест"
                    />
                    <RoomCard
                        img={Room3}
                        alt="Мастерская Успеха"
                        title="Мастерская Успеха"
                        description="11 мест"
                    />
                    <RoomCard
                        img={Room4}
                        alt="Пространство Идей"
                        title="Пространство Идей"
                        description="13 мест"
                    />
                    <RoomCard
                        img={Room5}
                        alt="Зона инноваций"
                        title="Зона инноваций"
                        description="8 мест"
                    />
                </Box>
        </>
    );
}
