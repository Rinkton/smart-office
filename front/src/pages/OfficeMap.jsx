import { Box, Typography } from "@mui/material";

export function OfficeMap() {
    return (
        <>
            <Typography
                variant="h6"
                style={{
                    padding: "10px 10px 30px 30px",
                    textAlign: "center"
                }}
            >
                Карта офиса
            </Typography>
            <Box
                sx={{
                    display: "flex",
                    flexDirection: "column",
                    gap: "20px",
                }}
            ></Box>
        </>
    );
}
