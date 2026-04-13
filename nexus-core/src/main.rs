use tonic::{transport::Server, Request, Response, Status};

//1. ดึงโค้ดที่Gen จากไฟล์ .proto มา่ใช้งาน
// (ชื่อ Package 'inventory' มาจากบรรทัด 'package inventory;' ในไฟล์.proto)
pub mod inventory {
    tonic::include_proto!("inventory");
}

//2. Import สิ่งที่จำเป็นมาจาก module ข้างบน
use inventory::inventory_service_server::{InventoryService, InventoryServiceServer};
use inventory::{DeductStockRequest, DeductStockResponse, GetItemRequest, GetItemResponse};

//3. สร้าง Struct ที่จะเป็นตัวแทนของ ร้านค้า ของเรา
#[derive(Debug, Default)]
pub struct MyInventory{}

//4. สร้าง Logic ให่กับร้านค้า (Implement Trait)
#[tonic::async_trait]
impl InventoryService for MyInventory{

    //Function: ดึงข้อมูลสินค้า
    async fn get_item(
        &self,
        request: Request<GetItemRequest>,
    ) -> Result<Response<GetItemResponse>, Status> {
        // แกะข้อมูลออกมาดู(ใน Console)
        println!("Got a request: {:?}", request);

        // เข้าถึงข้อมูลใน request ด้วย .into_inner()
        let req = request.into_inner();
        
        //สร้างคำตอบ (Mockup data ไปก่อน)
        let reply = GetItemResponse{
            product_id: req.product_id, // ส่ง ID เดิมกลับไป
            name: "Galaxy S24 Ultra".to_string(),
            quantity: 100,
            price: 45900.00,
        };

        // ส่งคำตอบกลับไป (ต้องห่อด้วย Ok และ Response)
        Ok(Response::new(reply))
    }

    // ฟังก์ชั่น: ตัดสต็อก
    async fn deduct_stock(
        &self,
        request: Request<DeductStockRequest>,
    ) -> Result<Response<DeductStockResponse>, Status> {

        println!("Deduct request: {:?}", request);
        let req = request.into_inner();

        // Mock ว่าตัดสำเร็จเสมอ
        let reply = DeductStockResponse {
            success: true,
            error_message: "".to_string(),
            remaining_quantity: 99, //สมมติว่าเหลือ99
        };

        Ok(Response::new(reply))
    }

}

// 5. Main Function (จุดเริ่มต้นของโปรแกรม)
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    
    // กำหนดที่อยู่  Server (0.0.0.0:50051)
    let addr = "[::1]:50051".parse()?

    // สร้าง Instance ของร้านค้า
    let inventory_service = MyInventory::default();

    println!("Nexus Core Server listening on {}", addr);

    // เริ่มรัน Server
    Server::builder()
        .add_service(InventoryServiceServer::new(inventory_service))
        .serve(addr)
        .await?;

    Ok(())
}
