#!/usr/bin/env python3
"""
Test script to verify quadrant-gen functionality
"""

def test_quadrant_gen_import():
    """Test if quadrant-gen can be imported successfully"""
    try:
        from quadrant_gen.chart import csv_to_quadrant_chart
        print("✓ Successfully imported quadrant_gen.chart.csv_to_quadrant_chart")
        return True
    except ImportError as e:
        print(f"✗ Failed to import quadrant-gen: {e}")
        return False

def test_chart_generation():
    """Test basic chart generation functionality"""
    try:
        from quadrant_gen.chart import csv_to_quadrant_chart
        
        # Sample CSV data
        sample_csv = """name,description,x,y
Product A,High quality,0.2,0.8
Product B,Low cost,0.7,0.3
Product C,Innovative,0.8,0.7
Product D,Traditional,0.3,0.2"""
        
        # Generate chart
        result = csv_to_quadrant_chart(
            csv_string=sample_csv,
            title="Test Quadrant Chart",
            x_left="Low X",
            x_right="High X",
            y_bottom="Low Y",
            y_top="High Y",
            format="png"
        )
        
        if result and result.startswith('data:image/png;base64,'):
            print("✓ Successfully generated PNG chart")
            return True
        else:
            print("✗ Chart generation failed - invalid result format")
            return False
            
    except Exception as e:
        print(f"✗ Chart generation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing quadrant-gen functionality...\n")
    
    tests = [
        ("Import Test", test_quadrant_gen_import),
        ("Chart Generation Test", test_chart_generation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}:")
        if test_func():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! quadrant-gen is working correctly.")
    else:
        print("❌ Some tests failed. Please check your quadrant-gen installation.")

if __name__ == "__main__":
    main()
