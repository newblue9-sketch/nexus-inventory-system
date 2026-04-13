package main

import (
	"github.com/gofiber/fiber/v2"
)

func main() {
	// 1. สร้างตึกหน้าบ้าน (Fiber App)
	app := fiber.New()

	// 2. โซนหน้าประตูบ้าน (Root)
	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello! Welcome to Nexus Gateway")
	})

	// 3. โซนโชว์สินค้า (Mock Data ไปก่อน)
	app.Get("/products", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"product_id": 1,
			"name":       "Super Car Audio System",
			"quantity":   10,
			"price":      15000.00,
		})
	})

	// 4. เปิดร้านรับลูกค้าที่พอร์ต 3000
	app.Listen(":3000")
}